import React, { Fragment } from "react";
import { PropTypes } from "prop-types";
import styles from "./auto-complete.module.scss";

//this component contains the part of autoComplete functionality for symptoms where the user gets a list 
//with symptom suggestions based on his input (view+functionality)
const Suggestions = ({
  suggestions,
  onSuggestionClick,
  suggestionNavigation,
  suggestionsRef,
}) => {
  return (
    <Fragment>
      {suggestions.length > 0 && (
        <ul className={styles.suggestions} ref={(ref) => suggestionsRef(ref)}>
          {suggestions.map((suggestion) => (
            <li
              key={suggestion}
              data-suggestion={suggestion}
              tabIndex="0"
              onClick={onSuggestionClick}
              onKeyUp={(e) => suggestionNavigation(e)}
            >
              {suggestion}
            </li>
          ))}
        </ul>
      )}
    </Fragment>
  );
};

Suggestions.propTypes = {
  suggestions: PropTypes.array.isRequired,
  onSuggestionClick: PropTypes.func.isRequired,
  suggestionNavigation: PropTypes.func.isRequired,
  suggestionsRef: PropTypes.func.isRequired,
};

Suggestions.defaultProps = {
  suggestions: [],
};

export default Suggestions;
