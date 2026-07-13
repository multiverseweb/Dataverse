// 3D Logo Implementation using Three.js
function init3DLogo() {
    const container = document.getElementById('logo-3d-container');
    if (!container) return;

    // Scene setup
    const scene = new THREE.Scene();

    // Camera setup
    const camera = new THREE.PerspectiveCamera(45, container.clientWidth / container.clientHeight, 0.1, 1000);
    camera.position.set(4, 3, 4);

    // Renderer setup
    const renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
    renderer.setSize(container.clientWidth, container.clientHeight);
    renderer.setPixelRatio(window.devicePixelRatio);
    container.appendChild(renderer.domElement);

    // Controls setup (Trackball for full rotation over all axes)
    const controls = new THREE.TrackballControls(camera, renderer.domElement);
    controls.rotateSpeed = 3.0;
    controls.zoomSpeed = 1.2;
    controls.noPan = true;
    controls.noZoom = false;
    controls.minDistance = 2;
    controls.maxDistance = 15;
    controls.dynamicDampingFactor = 0.15;

    // Axes and grids hidden as requested
    // const axesHelper = new THREE.AxesHelper(2.5);
    // scene.add(axesHelper);

    // const gridHelper = new THREE.GridHelper(6, 12, 0x444444, 0x222222);
    // gridHelper.position.y = -1.5;
    // scene.add(gridHelper);

    // Function to create gradient textures, matching exact CSS visual output
    function createGradient(direction, stops, cssRotate180, flipForThreeUV) {
        const canvas = document.createElement('canvas');
        canvas.width = 512;
        canvas.height = 512;
        const ctx = canvas.getContext('2d');
        
        let grd;
        if (direction === '90deg') { // L to R
            grd = ctx.createLinearGradient(0, 0, 512, 0);
        } else if (direction === '270deg') { // R to L
            grd = ctx.createLinearGradient(512, 0, 0, 0);
        }

        stops.forEach(s => grd.addColorStop(s.p, s.c));
        ctx.fillStyle = grd;
        ctx.fillRect(0, 0, 512, 512);

        // Apply CSS rotation if any
        let finalCanvas = canvas;
        if (cssRotate180) {
            finalCanvas = document.createElement('canvas');
            finalCanvas.width = 512; finalCanvas.height = 512;
            const fctx = finalCanvas.getContext('2d');
            fctx.translate(256, 256);
            fctx.rotate(Math.PI);
            fctx.drawImage(canvas, -256, -256);
        }

        // Apply UV flip for specific Three.js faces to ensure visual L to R on screen
        if (flipForThreeUV) {
            const flippedUVCanvas = document.createElement('canvas');
            flippedUVCanvas.width = 512; flippedUVCanvas.height = 512;
            const uctx = flippedUVCanvas.getContext('2d');
            uctx.translate(512, 0);
            uctx.scale(-1, 1);
            uctx.drawImage(finalCanvas, 0, 0);
            finalCanvas = flippedUVCanvas;
        }

        const texture = new THREE.CanvasTexture(finalCanvas);
        texture.needsUpdate = true;
        return texture;
    }

    // Define the 4 base gradients based on CSS
    const stops1 = [
        {p: 0, c: '#F1F624'}, {p: 0.165, c: '#FCCC25'}, {p: 0.275, c: '#F8880C'},
        {p: 0.39, c: '#DE5E65'}, {p: 0.48, c: '#C43F7F'}, {p: 0.555, c: '#A01A9C'},
        {p: 0.65, c: '#6F00A8'}, {p: 0.79, c: '#5302A3'}, {p: 1, c: '#130789'}
    ];
    const stops2 = [
        {p: 0, c: '#F4E41C'}, {p: 0.18, c: '#FDBE3D'}, {p: 0.32, c: '#AEBD67'},
        {p: 0.44, c: '#41BA97'}, {p: 0.555, c: '#25B4A9'}, {p: 0.655, c: '#05A3C9'},
        {p: 0.755, c: '#1078DA'}, {p: 0.845, c: '#1F52D3'}, {p: 1, c: '#352A86'}
    ];
    const stops3 = [
        {p: 0, c: '#C83B73'}, {p: 0.24, c: '#972C80'}, {p: 0.5275, c: '#50117B'},
        {p: 0.7525, c: '#221150'}, {p: 1, c: '#010106'}
    ];
    const stops4 = [
        {p: 0, c: '#440154'}, {p: 0.195, c: '#414487'}, {p: 0.405, c: '#2A788E'},
        {p: 0.6, c: '#22A884'}, {p: 0.79, c: '#7AD151'}, {p: 1, c: '#FDE725'}
    ];

    // Helper to generate a material
    function getMat(stops, dir, cssRot, flipUV) {
        return new THREE.MeshBasicMaterial({
            map: createGradient(dir, stops, cssRot, flipUV),
            transparent: true, opacity: 0.7, side: THREE.DoubleSide, depthWrite: false
        });
    }

    // Generate the materials for each specific face
    // Face 0: Right (UV u=1 is front, u=0 is back -> requires flip to go L to R visually)
    const matRight = getMat(stops2, '270deg', true, true); // Rect 9
    
    // Face 1: Left (UV u=0 is front, u=1 is back -> no flip needed)
    const matLeft = getMat(stops4, '90deg', true, false); // Rect 5 (Moved to side as requested)

    // Face 2: Top (UV u=0 is left, u=1 is right -> no flip needed)
    const matTop = getMat(stops3, '270deg', false, false); // Rect 10

    // Face 3: Bottom (UV u=0 is left, u=1 is right -> no flip needed)
    const matBottom = getMat(stops1, '90deg', false, false); // Rect 6 (User confirmed bottom is correct)

    // Face 4: Front (UV u=0 is left, u=1 is right -> no flip needed)
    const matFront = getMat(stops4, '90deg', true, false); // Rect 5

    // Face 5: Back (UV u=0 is right, u=1 is left -> requires flip)
    const matBack = getMat(stops2, '270deg', true, true); // Rect 9

    const materials = [
        matRight,  // 0: Right Face
        matLeft,   // 1: Left Face
        matTop,    // 2: Top Face
        matBottom, // 3: Bottom Face
        matFront,  // 4: Front Face
        matBack    // 5: Back Face
    ];

    const geometry = new THREE.BoxGeometry(2, 2, 2);
    const cube = new THREE.Mesh(geometry, materials);
    
    scene.add(cube);

    // Animation Loop
    function animate() {
        requestAnimationFrame(animate);
        // Manual auto-rotation (since TrackballControls lacks autoRotate)
        cube.rotation.y += 0.005;
        controls.update();
        renderer.render(scene, camera);
    }
    animate();

    // Resize Handler
    window.addEventListener('resize', () => {
        if (!container) return;
        camera.aspect = container.clientWidth / container.clientHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(container.clientWidth, container.clientHeight);
    });
}

document.addEventListener('DOMContentLoaded', init3DLogo);
