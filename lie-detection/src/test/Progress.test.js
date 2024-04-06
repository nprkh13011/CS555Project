import Progress from "../components/Progress.js";
import { fireEvent, getByText, render, screen } from "@testing-library/react";
import '@testing-library/jest-dom';
import { jest } from "@jest/globals";
import userEvent from '@testing-library/user-event';
import { act } from 'react-dom/test-utils'

it('Progress bar appears without crashing', () => {
    render(<Progress />);
});

it('bar hides the previous question button', () => {
    const { getByTestId } = render(<Progress />);
    const pagination = getByTestId('pagination');
    expect(pagination).toBeInTheDocument();
    expect(pagination).toHaveAttribute('hidePrevButton', 'true');
});