import React from "react";
import { PropTypes } from "prop-types";
import styles from "./info-card.module.scss";

//infocard is the component which is shown after user has entered his symptoms.
//Right now this component contains only Symptoms which were entered by user.
const InfoCard = ({ children }) => {
  return <article className={styles.infoCard}>{children}</article>;
};

InfoCard.propTypes = {
  children: PropTypes.node,
};

export default InfoCard;
