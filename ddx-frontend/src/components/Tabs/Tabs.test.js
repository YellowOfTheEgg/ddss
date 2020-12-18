import React from "react";
import { render, fireEvent } from "@testing-library/react";
import Tabs from "components/Tabs/Tabs";

test("render content of first tab by default", () => {
  const { queryByText } = render(
    <Tabs>
      <div label="Show All">All</div>
      <div label="Red Flagged">Flagged</div>
    </Tabs>
  );
  expect(queryByText("All")).toBeInTheDocument();
  expect(queryByText("Flagged")).not.toBeInTheDocument();
});

test("render content of the other tab on click", () => {
  const { queryByText, getByText } = render(
    <Tabs>
      <div label="Show All">All</div>
      <div label="Red Flagged">Flagged</div>
    </Tabs>
  );
  fireEvent.click(getByText("Red Flagged"));
  expect(queryByText("Flagged")).toBeInTheDocument();
  expect(queryByText("All")).not.toBeInTheDocument();
});
