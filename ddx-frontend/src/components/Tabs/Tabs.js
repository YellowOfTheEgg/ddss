import React, { useState } from "react";
import { PropTypes } from "prop-types";
import Tab from "./Tab";
import styles from "./tabs.module.scss";

// tabs contains 2 tabs: show all diagnoses and show first 3 after entering of the symptoms
const Tabs = ({ children }) => {
  const [activeTab, setActiveTab] = useState(children[0].props.label);

  const onClickTabItem = (tab) => {
    setActiveTab(tab);
  };

  return (
    <div className={styles.tabs}>
      <nav role="tablist">
        <ol className={styles.navList}>
          {children.map((child) => (
            <Tab
              activeTab={activeTab}
              key={child.props.label}
              label={child.props.label}
              onClick={onClickTabItem}
            />
          ))}
        </ol>
      </nav>
      <div className={styles.tabContent}>
        {children.map((child) => {
          if (child.props.label !== activeTab) return undefined;
          return child.props.children;
        })}
      </div>
    </div>
  );
};

Tabs.propTypes = {
  children: PropTypes.instanceOf(Array).isRequired,
};

export default Tabs;
