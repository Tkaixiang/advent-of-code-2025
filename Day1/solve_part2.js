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

    const amount = parseInt(cleanedLine.slice(1));

    // We now need to count everytime we PASS 0
    const remainder_amount = amount % 100;
    const numFullRotations = (amount - remainder_amount) / 100;
    count += numFullRotations;

    const prevDial = dial;
    dial += direction === "R" ? remainder_amount : -remainder_amount;
    if (dial > 99) {
      dial = dial - 100;
      if (prevDial !== 0) count += 1; // cause we would have counted it the last time we stopped at 0
    } else if (dial < 0) {
      dial += 100;
      if (prevDial !== 0) count += 1; // cause we would have counted it the last time we stopped at 0
    } else if (dial === 0) {
      count += 1;
    }
  }

  console.log(`Password is ${count}`);
};

start();
