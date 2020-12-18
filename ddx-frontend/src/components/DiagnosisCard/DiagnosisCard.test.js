import React from "react";
import { render } from "@testing-library/react";
import DiagnosisCard from "components/DiagnosisCard/DiagnosisCard";

const disease = {
  index: 1,
  name: "Influenza",
  code: "j10",
  description:
    "A viral infectious disease that results in infection, located in respiratory tract, has_material_basis_in Influenzavirus A, has_material_basis_inInfluenzavirus A viral infectious disease that results in infection, located in respiratory tract.",
  confidence: 2,
  isRedFlag: true,
};

test("confidence prop", () => {
  const { container } = render(<DiagnosisCard disease={disease} />);
  const [
    confidenceOne,
    confidenceTwo,
    confidenceThree,
    confidenceFour,
  ] = container.querySelectorAll("li");
  expect(confidenceOne.classList.contains("active")).toBeTruthy();
  expect(confidenceTwo.classList.contains("active")).toBeTruthy();
  expect(confidenceThree.classList.contains("active")).toBeFalsy();
  expect(confidenceFour.classList.contains("active")).toBeFalsy();
});

test("isRedFlag prop true", () => {
  const { container } = render(<DiagnosisCard disease={disease} />);
  expect(container.firstChild.classList.contains("redFlag")).toBeTruthy();
});

test("isRedFlag prop false", () => {
  disease.isRedFlag = false;
  const { container } = render(<DiagnosisCard disease={disease} />);
  expect(container.firstChild.classList.contains("redFlag")).toBeFalsy();
});
