import React from "react";
import { PropTypes } from "prop-types";
import styles from "./diagnosis-card.module.scss";

//this component contains the look of one diagnosis row which will be returned after a user enters his symptoms
const DiagnosisCard = ({ disease }) => {
  return (
    <article
      className={`
        ${styles.diagnosisCard}
        ${disease.isRedFlag ? styles.redFlag : ""}`}
    >
      <header className={styles.header}>
        <div className={styles.disease}>
          <div className={styles.index}>
            {disease.index ? disease.index : ""}
          </div>
          <div>
            <span className={styles.name}>
              {disease.name ? disease.name.toUpperCase() : ""}
            </span>
          </div>
        </div>

        <div className={styles.confidence}>
          <div>{disease.confidence}</div>
        </div>
      </header>
      <p className={styles.description}>
        {disease.description ? disease.description : ""}
      </p>
    </article>
  );
};

DiagnosisCard.propTypes = {
  disease: PropTypes.shape({
    index: PropTypes.number,
    name: PropTypes.string,
    confidence: PropTypes.number,
  }).isRequired,
};

export default DiagnosisCard;
