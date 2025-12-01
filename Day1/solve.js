import fs from "fs/promises";

const start = async () => {
  const data = await fs.readFile("input.txt", "utf-8");
  const lines = data.split("\n");
  let dial = 50;
  let count = 0;

  for (const line of lines) {
    const cleanedLine = line.trim();
    if (!cleanedLine) continue;
    const direction = cleanedLine[0];

    const amount = parseInt(cleanedLine.slice(1)) % 100;

    dial += direction === "R" ? amount : -amount;
    if (dial > 99) {
      dial = dial - 100;
    } else if (dial < 0) {
      dial += 100;
    }

    if (dial === 0) {
      count += 1;
    }
  }
  console.log(`Password is ${count}`);
};

start();
