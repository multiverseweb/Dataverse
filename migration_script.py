#!/usr/bin/env python3
"""
Migration script to update existing passwords to secure hashes
Run this ONCE after implementing the new security system

Usage: python migration_script.py
"""

import sys
import os

# Add software directory to path
sys.path.append('software')

import mysql.connector as my
from mysql.connector import Error
import db_config
from security import security_manager

def decrypt_old_password(encrypted_password):
    """
    Decrypt password using old method (for migration only)
    This function replicates the old decryption logic
    
    Args:
        encrypted_password (str): Old encrypted password
        
    Returns:
        str: Decrypted password
    """
    try:
        password_length = len(encrypted_password)
        decrypted_password = ""
        
        if password_length % 2 == 0:
            transformed_pwd = encrypted_password[int(password_length / 2):]
            transformed_pwd += encrypted_password[:int(password_length / 2)]
        else:
            transformed_pwd = encrypted_password[int(password_length / 2) + 1:]
            transformed_pwd += encrypted_password[:int(password_length / 2) + 1]
        
        for character in transformed_pwd:
            decrypted_password += chr(ord(character) // 2)
        
        return decrypted_password
    except Exception as e:
        print(f"Error decrypting old password: {e}")
        return None

def backup_database():
    """
    Create a backup of the user table before migration
    
    Returns:
        bool: True if backup successful
    """
    try:
        connection = my.connect(
            host=db_config.DB_HOST,
            user=db_config.DB_USER,
            password=db_config.DB_PASSWORD,
            database=db_config.DB_NAME
        )
        cursor = connection.cursor()
        
        # Create backup table
        backup_query = """
            CREATE TABLE IF NOT EXISTS user_backup_pre_security AS 
            SELECT * FROM user
        """
        cursor.execute(backup_query)
        connection.commit()
        
        print("✅ Database backup created successfully (user_backup_pre_security)")
        return True
        
    except Error as e:
        print(f"❌ Failed to create backup: {e}")
        return False
    finally:
        if connection:
            connection.close()

def migrate_passwords():
    """
    Migrate existing passwords to secure hashes
    
    Returns:
        bool: True if migration successful
    """
    try:
        connection = my.connect(
            host=db_config.DB_HOST,
            user=db_config.DB_USER,
            password=db_config.DB_PASSWORD,
            database=db_config.DB_NAME
        )
        cursor = connection.cursor()
        
        # Get all users with old password format
        cursor.execute("SELECT u_id, u_name, pwd FROM user")
        users = cursor.fetchall()
        
        if not users:
            print("ℹ️  No users found to migrate")
            return True
        
        migrated_count = 0
        failed_count = 0
        
        for u_id, username, old_pwd in users:
            try:
                # Check if password is already hashed (bcrypt hashes start with $2b$)
                if old_pwd.startswith('$2b$'):
                    print(f"⏭️  User {username} already has secure password, skipping")
                    continue
                
                # Decrypt old password
                decrypted = decrypt_old_password(old_pwd)
                if not decrypted:
                    print(f"❌ Failed to decrypt password for user: {username}")
                    failed_count += 1
                    continue
                
                # Hash with new secure method
                new_hash = security_manager.hash_password(decrypted)
                
                # Update database with parameterized query
                update_query = "UPDATE user SET pwd = %s WHERE u_id = %s"
                cursor.execute(update_query, (new_hash, u_id))
                
                migrated_count += 1
                print(f"✅ Migrated password for user: {username}")
                
            except Exception as e:
                print(f"❌ Failed to migrate password for user {username}: {e}")
                failed_count += 1
                continue
        
        connection.commit()
        
        print(f"\n📊 Migration Summary:")
        print(f"   ✅ Successfully migrated: {migrated_count} users")
        print(f"   ❌ Failed migrations: {failed_count} users")
        print(f"   📝 Total users processed: {len(users)} users")
        
        if failed_count == 0:
            print("\n🎉 Password migration completed successfully!")
        else:
            print(f"\n⚠️  Migration completed with {failed_count} failures")
        
        return failed_count == 0
        
    except Error as e:
        print(f"❌ Migration failed with database error: {e}")
        if connection:
            connection.rollback()
        return False
    except Exception as e:
        print(f"❌ Migration failed with unexpected error: {e}")
        if connection:
            connection.rollback()
        return False
    finally:
        if connection:
            connection.close()

def verify_migration():
    """
    Verify that migration was successful
    
    Returns:
        bool: True if verification successful
    """
    try:
        connection = my.connect(
            host=db_config.DB_HOST,
            user=db_config.DB_USER,
            password=db_config.DB_PASSWORD,
            database=db_config.DB_NAME
        )
        cursor = connection.cursor()
        
        # Check if all passwords are now bcrypt hashes
        cursor.execute("SELECT u_name, pwd FROM user")
        users = cursor.fetchall()
        
        non_bcrypt_count = 0
        for username, pwd in users:
            if not pwd.startswith('$2b$'):
                print(f"⚠️  User {username} still has non-bcrypt password")
                non_bcrypt_count += 1
        
        if non_bcrypt_count == 0:
            print("✅ Verification successful: All passwords are now securely hashed")
            return True
        else:
            print(f"❌ Verification failed: {non_bcrypt_count} users still have insecure passwords")
            return False
            
    except Error as e:
        print(f"❌ Verification failed: {e}")
        return False
    finally:
        if connection:
            connection.close()

def main():
    """Main migration function"""
    print("🔒 Dataverse Security Migration Script")
    print("=" * 50)
    
    # Check if .env file exists
    if not os.path.exists('.env'):
        print("❌ .env file not found!")
        print("Please create a .env file with your database configuration.")
        print("You can copy .env.example and modify it with your settings.")
        return False
    
    print("📋 Starting password migration process...")
    
    # Step 1: Create backup
    print("\n1️⃣  Creating database backup...")
    if not backup_database():
        print("❌ Backup failed. Migration aborted for safety.")
        return False
    
    # Step 2: Migrate passwords
    print("\n2️⃣  Migrating passwords to secure hashes...")
    if not migrate_passwords():
        print("❌ Migration failed. Please check the errors above.")
        return False
    
    # Step 3: Verify migration
    print("\n3️⃣  Verifying migration...")
    if not verify_migration():
        print("❌ Verification failed. Please check the migration manually.")
        return False
    
    print("\n🎉 Migration completed successfully!")
    print("\n📝 Next steps:")
    print("   1. Test login with existing users")
    print("   2. Create new users to test registration")
    print("   3. Remove backup table when satisfied: DROP TABLE user_backup_pre_security;")
    
    return True

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n⚠️  Migration interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)