import Home from "../components/Home";
import { fireEvent, getByText, render, screen } from "@testing-library/react";
import "@testing-library/jest-dom";
import { jest } from "@jest/globals";
import userEvent from "@testing-library/user-event";
import { MemoryRouter, Route, Router, Routes } from "react-router-dom";

test("redirect to ratings", async () => {
  let renderer = create(
    <MemoryRouter initialIndex={0} initialEntries={["/ratings"]}>
      <Routes>
        <Route path="ratings" element={<Home />}></Route>
      </Routes>
    </MemoryRouter>
  );
  await userEvent.click(await screen.findByText("View Professor Ratings"));
});
