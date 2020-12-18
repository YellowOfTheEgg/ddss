import React from 'react'
import { render } from '@testing-library/react'
import Stepper from 'components/Stepper/Stepper'

test('css class for the status of each step', () => {
  const { container } = render(<Stepper />)
  const steps = container.querySelectorAll('li')
  expect(steps[0].classList.contains('done')).toBeTruthy()
  expect(steps[1].classList.contains('todo')).toBeTruthy()
  expect(steps[2].classList.contains('todo')).toBeTruthy()
})