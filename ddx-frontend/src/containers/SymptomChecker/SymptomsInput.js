import React, { useState, useContext } from "react";
import qs from "qs";
import { SymptomCheckerContext } from "context/symptomCheckerContext";
import useDebounce from "hooks/useDebounce";
import { gatewayApi } from "api";
import AutoComplete from "components/AutoComplete/AutoComplete";
import Button from "components/Button/Button";
import InfoCard from "components/InfoCard/InfoCard";
import styles from "./symptom-checker.module.scss";

const SymptomsInput = () => {
  const [inputText, setInputText] = useState("");
  const [suggestions, setSuggestions] = useState([]);

  const [loadDiagnoses, setLoadDiagnoses] = useState(false);

  const {
    trueSymptoms,
    setTrueSymptoms,
    setDiagnoses,
    setCurrentStep,
  } = useContext(SymptomCheckerContext);

  const fetchDiagnoses = async () => {
    if (trueSymptoms.length < 1) return;

    setLoadDiagnoses(true);
    try {
      const options = {
        params: { symptoms: trueSymptoms },
        paramsSerializer: function (trueSymptoms) {
          return qs.stringify(trueSymptoms, { arrayFormat: "repeat" });
        },
      };

      const response = await gatewayApi.get("diagnoses/", options);
      const diagnosesData = response.data.body.diagnoses;
      if (diagnosesData.length > 0) {
        const formattedDiagnoses = await formatDiagnoses([...diagnosesData]);
        setDiagnoses(formattedDiagnoses);
        setLoadDiagnoses(false);
        setCurrentStep("Summary");
      }
    } catch (error) {
      console.error(error);
    }
  };

  const fetchAutofillSuggestions = async (searchTerm) => {
    try {
      const response = await gatewayApi.get("/symptoms", {
        params: {
          search_term: searchTerm,
        },
      });

      const symptoms = response.data.body.symptoms.slice(0, 9);
      setSuggestions(symptoms);
      return symptoms;
    } catch (error) {
      console.log(error);
    }
  };

  const debouncedGetSuggestions = useDebounce(fetchAutofillSuggestions, 300);

  const onInputChange = (text) => {
    text = text.trim();
    setInputText(text);
    debouncedGetSuggestions(text);
  };

  const clearAll = () => {
    setTrueSymptoms([]);
    setDiagnoses([]);
    setSuggestions([]);
    setInputText("");
  };

  const clearInput = () => {
    setInputText("");
    setSuggestions([]);
  };

  const removeSymptom = (e) => {
    const symptom = e.currentTarget.parentElement.innerText;
    if (!symptom) return;
    const newSymptoms = trueSymptoms.filter((symp) => symp !== symptom);
    setTrueSymptoms(newSymptoms);
  };

  const onAddTrueSymptomFromAutofill = (text) => {
    if (text === "") return;
    setTrueSymptoms([...trueSymptoms, text]);
    setInputText("");
  };

  const formatDiagnoses = (diagnoses) => {
    const sortedDiagnones = diagnoses.sort(
      (a, b) => b["probability"] - a["probability"]
    );
    const formattedDiagnoses = sortedDiagnones.map(async (diagnosis, i) => {
      console.log(diagnosis);
      const confidence = diagnosis.probability;
      return {
        index: i + 1,
        name: diagnosis.name,
        confidence,
      };
    });
    return Promise.all(formattedDiagnoses);
  };

  let symptom_container = "";
  let clear_button = "";

  if (trueSymptoms.length > 0) {
    symptom_container = (
      <div className={styles.symptomsContainer}>
        <ul className={styles.symptomsList}>
          {trueSymptoms.length > 0 &&
            trueSymptoms.map((symptom, index) => (
              <li key={index} className={styles.symptom}>
                {symptom}
                <span
                  className={styles.removeSymptom}
                  onClick={removeSymptom}
                ></span>
              </li>
            ))}
        </ul>
      </div>
    );
    clear_button = (
      <div className={styles.clearBtn}>
        <Button label="CLEAR ALL" variant="link" size="sm" onClick={clearAll} />
      </div>
    );
  }

  return (
    <div className={styles.symptomsInput}>
      <h1>Symptoms Input</h1>
      <InfoCard>
        <div className={styles.card}>
          {symptom_container}
          {clear_button}

          <div>
            <p className={styles.message}>
              What symptoms are bothering the most? <br />
              Please enter your symptoms and get possible diagnoses.
            </p>
            <AutoComplete
              inputText={inputText}
              placeholder="Search for symptoms eg. headache"
              onInputChange={onInputChange}
              suggestions={suggestions}
              onEnter={onAddTrueSymptomFromAutofill}
              onClear={clearInput}
            />
            <div className={styles.navButtons}>
              <Button
                label="Get Diagnoses"
                size="sm"
                onClick={fetchDiagnoses}
                loading={loadDiagnoses}
              />
            </div>
          </div>
        </div>
      </InfoCard>
    </div>
  );
};

export default SymptomsInput;
