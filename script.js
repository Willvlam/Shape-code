let currentInput = "0";
let pendingValue = "";
let currentOp = null;
const screen = document.getElementById('screen');

function update() {
    screen.innerText = currentInput;
}

function jsNum(n) {
    if (currentInput === "0") currentInput = n.toString();
    else currentInput += n.toString();
    update();
}

function jsReset() {
    currentInput = "0";
    pendingValue = "";
    currentOp = null;
    update();
}

function jsOp(op) {
    currentOp = op;
    pendingValue = currentInput;
    currentInput = "0";
}

function jsEqual() {
    if (!currentOp) return;
    let result = eval(pendingValue + currentOp + currentInput);
    currentInput = result.toString();
    currentOp = null;
    update();
}

// Scientific Math (Trig)
function jsMath(type) {
    let val = parseFloat(currentInput);
    // Standard trig in JS uses Radians, so we convert to Degrees
    let rad = val * (Math.PI / 180);
    
    if (type === 'sin') currentInput = Math.sin(rad).toFixed(4);
    if (type === 'cos') currentInput = Math.cos(rad).toFixed(4);
    if (type === 'tan') currentInput = Math.tan(rad).toFixed(4);
    update();
}

function jsToggle() {
    currentInput = (parseFloat(currentInput) * -1).toString();
    update();
}

// INTEGRATED 2 SPEEDRUNS
function jsGrowth() {
    let p = parseFloat(prompt("Principal:"));
    let r = parseFloat(prompt("Rate %:")) / 100;
    let t = parseFloat(prompt("Years:"));
    let n = prompt("Compounding (1=Yearly, 12=Monthly, 0=Cont):") || 1;
    let res = (n == "0") ? p * Math.exp(r * t) : p * Math.pow((1 + r/n), (n * t));
    currentInput = res.toFixed(2);
    update();
}

function jsDecay() {
    let p = parseFloat(prompt("Initial Value:"));
    let r = parseFloat(prompt("Decay %:")) / 100;
    let t = parseFloat(prompt("Years:"));
    currentInput = (p * Math.pow((1 - r), t)).toFixed(2);
    update();
}

function jsQuad() {
    let a = parseFloat(prompt("a:"));
    let b = parseFloat(prompt("b:"));
    let c = parseFloat(prompt("c:"));
    let d = (b*b) - (4*a*c);
    if (d < 0) {
        alert("Imaginary Roots");
    } else {
        let x1 = ((-b + Math.sqrt(d))/(2*a)).toFixed(2);
        let x2 = ((-b - Math.sqrt(d))/(2*a)).toFixed(2);
        alert(`x1: ${x1}, x2: ${x2}`);
        currentInput = x1;
        update();
    }
}

function jsAngle() {
    let n = parseInt(prompt("Sides:"));
    let type = prompt("1: Interior, 2: Exterior");
    currentInput = (type == "1") ? ((n-2)*180/n).toFixed(1) : (360/n).toFixed(1);
    update();
}