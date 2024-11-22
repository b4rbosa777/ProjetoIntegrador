import React from 'react';
import styles from './DataCard.module.css';

const DataCard = ({ title, value, unit, icon }) => {
  return (
    <div className={styles.card}>
      <div className={styles.iconContainer}>{icon}</div>
      <div className={styles.valueContainer}>
        <span className={styles.value}>{value}</span>
        {unit && <span className={styles.unit}>{unit}</span>}
      </div>
      <p className={styles.title}>{title}</p>
    </div>
  );
};

export default DataCard;
