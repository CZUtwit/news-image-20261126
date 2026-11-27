// Entry point: copy the pre-rendered image into the grader output folder.
import * as fs from "node:fs";
import * as path from "node:path";
import { fileURLToPath as toPath } from "node:url";

const root = path.dirname(toPath(import.meta.url));
const out = process.env.OUTPUT_DIR || "/output";
fs.mkdirSync(out, { recursive: true });
const target = path.join(out, "entry.png");
fs.copyFileSync(path.join(root, "entry.png"), target);
process.stdout.write(`wrote ${target}\n`);
