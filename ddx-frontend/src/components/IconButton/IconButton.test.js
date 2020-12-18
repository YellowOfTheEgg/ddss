import React from "react";
import { render, fireEvent } from "@testing-library/react";
import IconButton from "components/IconButton/IconButton";

test("add default css classes", () => {
  const { container } = render(<IconButton />);
  expect(container.firstChild.classList.contains("iconButton")).toBeTruthy();
  expect(container.firstChild.classList.contains("download")).toBeTruthy();
  expect(container.firstChild.classList.contains("md")).toBeTruthy();
});

test("size prop", () => {
  const { container } = render(<IconButton size="sm" />);
  expect(container.firstChild.classList.contains("sm")).toBeTruthy();
});

test("icon prop", () => {
  const { container } = render(<IconButton icon="share" />);
  expect(container.firstChild.classList.contains("share")).toBeTruthy();
});

test("onClick prop", () => {
  const mockCallBack = jest.fn();
  const { container } = render(<IconButton onClick={mockCallBack} />);
  fireEvent.click(container.firstChild);
  expect(mockCallBack).toHaveBeenCalled();
});

test("label prop", () => {
  const { getByText } = render(<IconButton label="Download" />);
  const label = getByText("Download");
  expect(label).toBeInTheDocument();
});
