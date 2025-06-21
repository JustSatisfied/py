const { spawn } = require('child_process');

const pythonScript = 'analysis.py';

const pythonProcess = spawn('python', [pythonScript]);

console.log(`Node.js 已启动 Python 进程，PID: ${pythonProcess.pid}`);

pythonProcess.stdout.on('data', (data) => {
  console.log(`Python stdout: ${data.toString()}`);
});

pythonProcess.stderr.on('data', (data) => {
  console.error(`Python stderr: ${data.toString()}`);
});

pythonProcess.on('close', (code) => {
  console.log(`Python process exited with code ${code}`);
});

pythonProcess.on('error', (err) => {
  console.error(`Failed to start Python process: ${err}`);
});

while (true){
    
}