const fs = require('fs');
const inputFilePath = 'day18-input.txt';

const WIDTH = 7; // Change to 71 for the actual puzzle
const HEIGHT = 7; // Change to 71 for the actual puzzle

// Read the input file
const input = fs.readFileSync(inputFilePath, 'utf-8').trim().split('\n').map(line => line.split(',').map(Number));

// Create the memory space grid
let grid = Array.from({ length: HEIGHT }, () => Array(WIDTH).fill('.'));

// Simulate the falling bytes
input.slice(0, 1024).forEach(([x, y]) => {
    if (x >= 0 && x < WIDTH && y >= 0 && y < HEIGHT) {
        grid[y][x] = '#';
    }
});

// Display the grid
grid.forEach(row => console.log(row.join('')));

// Find the shortest path using Breadth-First Search (BFS)
const directions = [
    [0, 1],  // Down
    [1, 0],  // Right
    [0, -1], // Up
    [-1, 0]  // Left
];

const bfs = (grid, start, goal) => {
    const queue = [[start]];
    const visited = new Set();
    visited.add(`${start[0]},${start[1]}`);

    while (queue.length) {
        const path = queue.shift();
        const [x, y] = path[path.length - 1];

        if (x === goal[0] && y === goal[1]) {
            return path.length - 1;
        }

        for (const [dx, dy] of directions) {
            const newX = x + dx;
            const newY = y + dy;

            if (
                newX >= 0 && newX < WIDTH &&
                newY >= 0 && newY < HEIGHT &&
                grid[newY][newX] === '.' &&
                !visited.has(`${newX},${newY}`)
            ) {
                visited.add(`${newX},${newY}`);
                queue.push([...path, [newX, newY]]);
            }
        }
    }

    return -1; // No path found
};

const start = [0, 0];
const goal = [6, 6]; // Change to [70, 70] for the actual puzzle
const shortestPathLength = bfs(grid, start, goal);

console.log(`Minimum number of steps needed to reach the exit: ${shortestPathLength}`);
