
import { render, screen } from '@testing-library/react';
import LoginForm from '../../client/src/components/LoginForm';

test('renders login form', () => {
  render(<LoginForm />);
  const emailField = screen.getByPlaceholderText(/email/i);
  expect(emailField).toBeInTheDocument();
});
