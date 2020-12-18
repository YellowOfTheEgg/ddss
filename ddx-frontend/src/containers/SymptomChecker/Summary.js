import React, { useContext } from "react";
import { SymptomCheckerContext } from "context/symptomCheckerContext";
import Button from "components/Button/Button";
import InfoCard from "components/InfoCard/InfoCard";
import Tabs from "components/Tabs/Tabs";
import DiagnosisCard from "components/DiagnosisCard/DiagnosisCard";
import styles from "./symptom-checker.module.scss";


//this container defines the view of the diagnosis results
const Summary = () => {
  const {
    setCurrentStep,
    trueSymptoms,
    setTrueSymptoms,
    diagnoses,
    setDiagnoses,
  } = useContext(SymptomCheckerContext);

  const onStartOver = () => {
    setTrueSymptoms([]);
    setDiagnoses([]);
    setCurrentStep("Symptoms Input");
  };

  const renderSymptoms = () => (
    <InfoCard>
      <h2>Positiv symptoms</h2>
      <div>
        <div style={{ display: "flex", justifyContent: "center" }}>
          <ul className={styles.symptoms}>
            {trueSymptoms.map((symptom) => (
              <li key={symptom}>{symptom}</li>
            ))}
          </ul>
        </div>
      </div>
    </InfoCard>
  );

  const renderDiagnoses = () => (
    <InfoCard>
      <h2>Diagnoses</h2>
      <div className={styles.diagnoses}>
        <Tabs>
          <div label="Show All">
            <div className={styles.list}>
              {diagnoses.map((disease) => (
                <DiagnosisCard key={disease.index} disease={disease} />
              ))}
            </div>
          </div>

          <div label="Top 3" className={styles.list}>
            <div className={styles.list}>
              {diagnoses.slice(0, 3).map((disease) => (
                <DiagnosisCard key={disease.index} disease={disease} />
              ))}
            </div>
          </div>
        </Tabs>
      </div>
    </InfoCard>
  );

  return (
    <div className={styles.summary}>
      <div className={styles.header}>
        <h1>Summary</h1>
      </div>

      {renderSymptoms()}

      {renderDiagnoses()}

      <div className={styles.buttonContainer}>
        <Button label="START OVER" onClick={onStartOver} />
      </div>
    </div>
  );
};

export default Summary;
