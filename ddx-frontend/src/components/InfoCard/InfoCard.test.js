import React from "react";
import { render } from "@testing-library/react";
import InfoCard from "components/InfoCard/InfoCard";

test("render props.children", () => {
  const { getByText } = render(
    <InfoCard>
      <h2>InfoCard</h2>
      <div>Information</div>
    </InfoCard>
  );
  const title = getByText("InfoCard");
  const body = getByText("Information");
  expect(title).toBeInTheDocument();
  expect(body).toBeInTheDocument();
});
