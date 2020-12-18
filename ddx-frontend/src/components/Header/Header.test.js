import React from "react";
import { BrowserRouter, Router } from "react-router-dom";
import { render, fireEvent } from "@testing-library/react";
import { createMemoryHistory } from "history";
import Header from "components/Header/Header";

test("default css classes", () => {
  const { container } = render(
    <BrowserRouter>
      <Header />
    </BrowserRouter>
  );
  expect(container.firstChild.classList.contains("header")).toBeTruthy();
});

test("Symptom Checker NavLink", () => {
  const history = createMemoryHistory();
  const { getByText } = render(
    <Router history={history}>
      <Header />
    </Router>
  );
  const navLink = getByText("Symptom Checker");
  fireEvent.click(navLink);
  expect(history.location.pathname).toBe("/ddx");
  expect(navLink.classList.contains("active")).toBeTruthy();
});

test("Feedback NavLink", () => {
  const history = createMemoryHistory();
  const { getByText } = render(
    <Router history={history}>
      <Header />
    </Router>
  );
  const navLink = getByText("Feedback");
  fireEvent.click(navLink);
  expect(history.location.pathname).toBe("/feedback");
  expect(navLink.classList.contains("active")).toBeTruthy();
});
