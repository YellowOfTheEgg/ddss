import React from "react";
import { render, fireEvent } from "@testing-library/react";
import AutoComplete from "./AutoComplete";

const suggestions = ["fever", "pain", "strong pain"];

test("show suggestions passed as prop", () => {
  const { container } = render(
    <AutoComplete
      suggestions={suggestions}
      onInputChange={jest.fn()}
      onClear={jest.fn()}
      onEnter={jest.fn()}
    />
  );
  const listOfSuggestions = container.querySelectorAll("li");
  expect(listOfSuggestions.length).toBe(3);
});

test("on suggestion click, change input text and hide suggestions", async () => {
  const mockOnInputChange = jest.fn();
  const { getByText, container } = render(
    <AutoComplete
      suggestions={suggestions}
      onInputChange={mockOnInputChange}
      onClear={jest.fn()}
      onEnter={jest.fn()}
    />
  );
  const suggestion = getByText("pain");
  fireEvent.click(suggestion);
  expect(container.querySelector("ul")).toBeFalsy();
  expect(mockOnInputChange).toHaveBeenCalledWith("pain");
});

test("on suggestion enter key, change input text and hide suggestions", async () => {
  const mockOnInputChange = jest.fn();
  const { getByText, container } = render(
    <AutoComplete
      suggestions={suggestions}
      onInputChange={mockOnInputChange}
      onClear={jest.fn()}
      onEnter={jest.fn()}
    />
  );
  const suggestion = getByText("fever");
  fireEvent.keyUp(suggestion, { key: "Enter" });
  expect(container.querySelector("ul")).toBeFalsy();
  expect(mockOnInputChange).toHaveBeenCalledWith("fever");
});
