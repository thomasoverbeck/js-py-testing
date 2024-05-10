import fs from "fs";
import YAML from "yaml";
import { describe, expect, it } from "@jest/globals";
import { Calculator } from "./calculator";

const file = fs.readFileSync("./testcases.yaml", "utf8");
const suite = YAML.parse(file).suite;

let calculator;

describe("calculator", () => {
  beforeEach(() => {
    calculator = new Calculator();
  });

  for (const unit of suite) {
    describe(unit.name, () => {
      it('is a function', () => {
        expect(typeof calculator[unit.name]).toBe("function");
      });

      it.each(unit.tests)("$description", ({ description, input, output }) => {
        const result = calculator[unit.name](...input);

        expect(result).toBe(output);
      });
    });
  }
});
