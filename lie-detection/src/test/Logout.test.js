import Logout from "../components/Logout"
import {fireEvent, getByText, render, screen} from "@testing-library/react";
import '@testing-library/jest-dom';
import { jest } from "@jest/globals";
import userEvent from '@testing-library/user-event';
import {act} from 'react-dom/test-utils'

//incomplete
it("should render the page correctly", () => {
    render(<Logout/>)
    // const logoutt = screen.getByText("Sign Up")

    // expect(logoutt).toHaveBeenCalled();
});
