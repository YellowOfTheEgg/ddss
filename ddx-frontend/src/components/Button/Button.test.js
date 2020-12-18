import React from "react";
import { render, fireEvent } from "@testing-library/react";
import Button from "components/Button/Button";

test("add default css classes", () => {
  const { container } = render(<Button label="Submit" />);
  expect(container.firstChild.classList.contains("button")).toBeTruthy();
  expect(container.firstChild.classList.contains("primary")).toBeTruthy();
  expect(container.firstChild.classList.contains("md")).toBeTruthy();
});

test("label prop", () => {
  const { getByText } = render(<Button label="Submit" />);
  const label = getByText(/Submit/i);
  expect(label).toBeInTheDocument();
});

test("variant prop", () => {
  const { container } = render(<Button label="Submit" variant="ghost" />);
  expect(container.firstChild.classList.contains("ghost")).toBeTruthy();
});

test("type prop", () => {
  const { container } = render(<Button label="Submit" type="submit" />);
  expect(container.firstChild).toHaveAttribute("type");
});

test("size prop", () => {
  const { container } = render(<Button label="Submit" size="lg" />);
  expect(container.firstChild.classList.contains("lg")).toBeTruthy();
});

test("disabled prop", () => {
  const { container } = render(<Button label="Submit" disabled={true} />);
  expect(container.firstChild).toHaveAttribute("disabled");
});

test("onClick prop", () => {
  const mockCallBack = jest.fn();
  const { container } = render(
    <Button label="Submit" onClick={mockCallBack} />
  );
  fireEvent.click(container.firstChild);
  expect(mockCallBack).toHaveBeenCalled();
});
