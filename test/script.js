// script.js

// Get the front and back canvases and SVGs
const frontCanvas = document.getElementById('front-canvas');
const backCanvas = document.getElementById('back-canvas');
const frontBodySVG = document.getElementById('front-body');
const backBodySVG = document.getElementById('back-body');

// Get the drawing contexts
const frontContext = frontCanvas.getContext('2d');
const backContext = backCanvas.getContext('2d');

// Set canvas dimensions to match SVG dimensions
frontCanvas.width = 200;
frontCanvas.height = 400;
backCanvas.width = 200;
backCanvas.height = 400;

// Set up event listeners for drawing
let drawing = false;
let strokeColor = 'red';
let currentCanvas = frontCanvas;

frontCanvas.addEventListener('mousedown', startDrawing);
backCanvas.addEventListener('mousedown', startDrawing);
frontCanvas.addEventListener('mousemove', draw);
backCanvas.addEventListener('mousemove', draw);
window.addEventListener('mouseup', stopDrawing);

// Variables to track drawing state
let lastX, lastY;

function startDrawing(e) {
  drawing = true;
  [lastX, lastY] = [e.clientX - e.target.getBoundingClientRect().left, e.clientY - e.target.getBoundingClientRect().top];
}
// Set up event listeners for Clear buttons
const clearFrontButton = document.getElementById('clear-front-button');
const clearBackButton = document.getElementById('clear-back-button');

clearFrontButton.addEventListener('click', clearCanvas.bind(null, 'front-canvas', 'frontContext'));
clearBackButton.addEventListener('click', clearCanvas.bind(null, 'back-canvas', 'backContext'));

function clearCanvas(canvasId, contextId) {
  const canvas = document.getElementById(canvasId);
  const context = canvas.getContext('2d');
  context.clearRect(0, 0, canvas.width, canvas.height);
}

// Update the draw function to store drawing history
function draw(e) {
  if (!drawing) return;
  const x = e.clientX - e.target.getBoundingClientRect().left;
  const y = e.clientY - e.target.getBoundingClientRect().top;

  let context = e.target.id === 'front-canvas' ? frontContext : backContext;
  context.lineJoin = 'round';
  context.lineCap = 'round';
  context.lineWidth = 5;
  context.strokeStyle = strokeColor;

  context.beginPath();
  context.moveTo(lastX, lastY);
  context.lineTo(x, y);
  context.stroke();

  [lastX, lastY] = [x, y];

}

// Set up event listeners for color-changing buttons
const colorRedButton = document.getElementById('color-red');
const colorBlueButton = document.getElementById('color-blue');

colorRedButton.addEventListener('click', () => {
  strokeColor = 'red';
  updateStrokeColor();
});

colorBlueButton.addEventListener('click', () => {
  strokeColor = 'blue';
  updateStrokeColor();
});

// Function to update the stroke color
function updateStrokeColor() {
  console.log("updating color", strokeColor)
  frontContext.strokeStyle = strokeColor;
  backContext.strokeStyle = strokeColor;
}

function stopDrawing() {
  drawing = false;
}

// Save drawings as PNG images
const saveButton = document.getElementById('save-button');
saveButton.addEventListener('click', () => {
  // Convert front canvas to PNG
  const frontImageData = frontCanvas.toDataURL('image/png');
  downloadImage(frontImageData, 'front-drawing.png');

  // Convert back canvas to PNG
  const backImageData = backCanvas.toDataURL('image/png');
  downloadImage(backImageData, 'back-drawing.png');
});

function downloadImage(dataUrl, filename) {
  const a = document.createElement('a');
  a.href = dataUrl;
  a.download = filename;
  a.style.display = 'none';
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
}
