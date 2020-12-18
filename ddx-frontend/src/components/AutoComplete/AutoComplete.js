import React, { useState, useEffect, useRef } from "react";
import { PropTypes } from "prop-types";
import Suggestions from "./Suggestions";
import styles from "./auto-complete.module.scss";


//this component contains the autoComplete functionality for symptoms (view+functionality)
const AutoComplete = ({
  inputText,
  onInputChange,
  placeholder,
  suggestions,
  onEnter,
  onClear,
}) => {
  const [showSuggestion, setShowSuggestion] = useState(true);
  let suggestionsRef = useRef();
  let autoCompleteRef = useRef();

  useEffect(() => {
    // Add event listener only when the suggestions are visible
    if (suggestions.length > 0) {
      document.addEventListener("mousedown", handleClickOutside, false);
    } else {
      document.removeEventListener("mousedown", handleClickOutside, false);
    }
  });

  const handleClickOutside = (e) => {
    if (
      autoCompleteRef.current &&
      !autoCompleteRef.current.contains(e.target)
    ) {
      // check if click was not on the suggestions
      setShowSuggestion(false);
    }
  };

  const suggestionNavigation = (e) => {
    if (e.key === "Enter") {
      if (!e.currentTarget.hasAttribute("data-suggestion")) {
        // Enter on input element
        onEnter(inputText);
        setShowSuggestion(false);
        return;
      }
      // Enter on the suggestion
      const suggestion = e.currentTarget.getAttribute("data-suggestion");
      onInputChange(suggestion);
      setShowSuggestion(false);
    }

    if (suggestions.length !== 0) {
      if (e.key === "Enter") {
        const suggestion = e.currentTarget.getAttribute("data-suggestion");
        if (!suggestion) return;
        onInputChange(suggestion);
        onEnter(suggestion);
        setShowSuggestion(false);
      }

      if (e.key === "ArrowDown" && e.target.tagName === "INPUT") {
        return (
          suggestionsRef &&
          suggestionsRef
            .querySelector("ul > li:first-child")
            .focus({ preventScroll: true })
        );
      }

      if (e.key === "ArrowDown" && e.target.tagName === "LI") {
        return (
          e.target.nextElementSibling &&
          e.target.nextElementSibling.focus({ preventScroll: true })
        );
      }

      if (e.key === "ArrowUp" && e.target.tagName === "LI") {
        return (
          e.target.previousElementSibling &&
          e.target.previousElementSibling.focus({ preventScroll: true })
        );
      }
    }
  };

  const onInputTextChange = (e) => {
    const text = e.target.value;
    if (text === undefined) return;

    if (text.length === 0) {
      setShowSuggestion(false);
    } else {
      setShowSuggestion(true);
    }

    onInputChange(text);
  };

  const onSuggestionClick = (e) => {
    const suggestion = e.currentTarget.getAttribute("data-suggestion");
    if (!suggestion) return;
    onInputChange(suggestion);
    onEnter(suggestion);
    setShowSuggestion(false);
  };

  return (
    <div className={styles.autoComplete} ref={autoCompleteRef}>
      <input
        type="text"
        placeholder={placeholder}
        value={inputText}
        onChange={onInputTextChange}
        onKeyUp={(e) => suggestionNavigation(e)}
      />
      {showSuggestion && inputText && (
        <span className={styles.clear} onClick={onClear}></span>
      )}
      {showSuggestion && (
        <Suggestions
          suggestions={suggestions}
          suggestionNavigation={suggestionNavigation}
          onSuggestionClick={onSuggestionClick}
          suggestionsRef={(ref) => (suggestionsRef = ref)}
        />
      )}
    </div>
  );
};

AutoComplete.propTypes = {
  placeholder: PropTypes.string,
  onInputChange: PropTypes.func.isRequired,
  onClear: PropTypes.func.isRequired,
  onEnter: PropTypes.func.isRequired,
  inputText: PropTypes.string,
  suggestions: PropTypes.array,
};

AutoComplete.defaultProps = {
  suggestions: [],
  placeholder: "",
  inputText: "",
};

export default AutoComplete;
