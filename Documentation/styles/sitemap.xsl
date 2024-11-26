<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:sitemap="http://www.sitemaps.org/schemas/sitemap/0.9">
    <xsl:output method="html" indent="yes" />

    <xsl:template match="/">
        <html>
            <head>
                <title>Sitemap</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        line-height:30px;
                        background-color:#000000;
                        color:#ffffff;
                    }
                    h1 {
                        text-align: center;
                        margin: 20px 0;
                    }
                    table {
                        margin: 20px auto;
                        border-collapse: collapse;
                        width:100%;
                        font-size:20px;
                    }
                    th, td {
                        border: 1px solid #ffffff00;
                        padding: 10px;
                        text-align: left;
                    }
                    th {
                        background-color: #2e2e2e;
                    }
                    tr:nth-child(even) {
                        background-color: #1a1a1a;
                    }
                    a{
                        color:#00dbe3;
                    }
                </style>
            </head>
            <body>
                <h1>Sitemap</h1>
                <table>
                    <tr>
                        <th>URL</th>
                        <th>Last Modified</th>
                        <th>Change Freq.</th>
                        <th>Priority</th>
                    </tr>
                    <xsl:for-each select="sitemap:urlset/sitemap:url">
                        <tr>
                            <td><a href="{sitemap:loc}"><xsl:value-of select="sitemap:loc" /></a></td>
                            <td><xsl:value-of select="sitemap:lastmod" /></td>
                            <td><xsl:value-of select="sitemap:changefreq" /></td>
                            <td><xsl:value-of select="sitemap:priority" /></td>
                        </tr>
                    </xsl:for-each>
                </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>



