import { useRef } from "react";
// this component is used for a data-stream-simulating.
//it is needed for symptoms suggestions based on what user has entered.
const debounce = (fn, delay) => {
  let timeout;
  return function (...args) {
    if (timeout) {
      clearTimeout(timeout);
    }
    timeout = setTimeout(() => {
      fn(...args);
    }, delay);
  };
};

const useDebounce = (func, delay) => {
  const debouncedFunc = useRef(debounce(func, delay)).current;

  return debouncedFunc;
};

export default useDebounce;
