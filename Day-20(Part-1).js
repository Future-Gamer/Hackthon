const fs = require('fs');

// Directions for movement: up, down, left, right
const DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]];

// Helper function to perform BFS
function bfs(mapGrid, start, end, cheatAllowed) {
    const rows = mapGrid.length;
    const cols = mapGrid[0].length;
    const queue = [[start[0], start[1], 0, cheatAllowed]];  // [row, col, time_taken, is_cheating]
    const visited = new Set();  // To keep track of visited positions (row, col, cheat status)
    visited.add(`${start[0]},${start[1]},${cheatAllowed}`);

    while (queue.length > 0) {
        const [x, y, time, usedCheat] = queue.shift();

        // If we reached the end, return the time taken
        if (x === end[0] && y === end[1]) {
            return time;
        }

        // Try moving in all four possible directions
        for (let [dx, dy] of DIRECTIONS) {
            const nx = x + dx;
            const ny = y + dy;

            // Check if the new position is within bounds
            if (nx >= 0 && nx < rows && ny >= 0 && ny < cols) {
                const cell = mapGrid[nx][ny];

                // If not cheating and hitting a wall, skip
                if (!usedCheat && cell === '#') {
                    continue;
                }

                // If cheating, we allow walls to be passed
                if (cell === '#' && !usedCheat) {
                    // Cheat used: pass through wall for 1 picosecond
                    if (!visited.has(`${nx},${ny},true`)) {
                        visited.add(`${nx},${ny},true`);
                        queue.push([nx, ny, time + 1, true]);
                    }
                } else {
                    if (!visited.has(`${nx},${ny},${usedCheat}`)) {
                        visited.add(`${nx},${ny},${usedCheat}`);
                        queue.push([nx, ny, time + 1, usedCheat]);
                    }
                }
            }
        }
    }

    return Infinity;  // Return infinity if no path found
}

// Function to calculate the number of cheats saving at least 100 picoseconds
function calculateCheats(mapGrid, start, end) {
    // First, compute the shortest path without cheating
    const normalTime = bfs(mapGrid, start, end, false);

    // Collect all possible cheats that might save time
    const cheats = [];
    const rows = mapGrid.length;
    const cols = mapGrid[0].length;

    // Check all positions on the map for potential cheating opportunities
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            if (mapGrid[i][j] === '.') {
                // Try cheating from this position and check the time
                const timeWithCheat = bfs(mapGrid, start, [i, j], true) + bfs(mapGrid, [i, j], end, true);

                if (timeWithCheat < normalTime) {
                    cheats.push(normalTime - timeWithCheat);  // Track time saved by the cheat
                }
            }
        }
    }

    // Sort cheats in descending order to prioritize saving the most time
    cheats.sort((a, b) => b - a);

    // Count cheats that save at least 100 picoseconds
    let count = 0;
    for (let cheat of cheats) {
        if (cheat >= 100) {
            count++;
        }
    }

    return count;
}

// Main function to read input file and start the process
function main() {
    // Read input data from the file
    const filename = 'day20-input.txt';  // Input file with the racetrack map
    const mapGrid = fs.readFileSync(filename, 'utf-8').split('\n').map(line => line.split(''));

    // Find the start (S) and end (E) positions
    let start = null;
    let end = null;

    for (let r = 0; r < mapGrid.length; r++) {
        for (let c = 0; c < mapGrid[r].length; c++) {
            if (mapGrid[r][c] === 'S') start = [r, c];
            if (mapGrid[r][c] === 'E') end = [r, c];
        }
    }

    // Start the execution timer
    console.time('Execution Time');

    // Calculate and print the result
    const result = calculateCheats(mapGrid, start, end);
    console.log(`Number of cheats saving at least 100 picoseconds: ${result}`);

    // End the execution timer
    console.timeEnd('Execution Time');
}

// Execute the main function
main();
