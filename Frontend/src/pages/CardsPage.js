import React, { useState, useEffect } from 'react';
import axios from 'axios';
import DataCard from '../components/DataCard/DataCard';
import { FaThermometerHalf, FaTint, FaWater } from 'react-icons/fa';
 
const CardsPage = () => {
  // Estado para dados dos sensores
  const [sensorData, setSensorData] = useState({
    temperature: 0,
    airHumidity: 0,
    soilMoisture: 0,
  });
 
  // Função para buscar dados de temperatura
  const fetchTemperature = async () => {
    try {
      const response = await axios.get('http://localhost:5271/api/Temperatura');
      const data = response.data && response.data.length > 0 ? response.data[response.data.length - 1] : null; // Pega o último item
      if (data) {
        setSensorData(prevData => ({
          ...prevData,
          temperature: data.temperaturaAtual || 0,
        }));
      }
    } catch (error) {
      console.error("Erro ao buscar dados de temperatura:", error);
    }
  };
 
  // Função para buscar dados de umidade do ar
  const fetchAirHumidity = async () => {
    try {
      const response = await axios.get('http://localhost:5271/api/Umidade');
      const data = response.data && response.data.length > 0 ? response.data[response.data.length - 1] : null; // Pega o último item
      if (data) {
        setSensorData(prevData => ({
          ...prevData,
          airHumidity: data.umidadeAtual || 0,
        }));
      }
    } catch (error) {
      console.error("Erro ao buscar dados de umidade do ar:", error);
    }
  };
 
  // Função para buscar dados de umidade do solo
  const fetchSoilMoisture = async () => {
    try {
      const response = await axios.get('http://localhost:5271/api/UmidadeTerra');
      const data = response.data && response.data.length > 0 ? response.data[response.data.length - 1] : null; // Pega o último item
      if (data) {
        setSensorData(prevData => ({
          ...prevData,
          soilMoisture: data.umidadeTerraAtual || 0,
        }));
      }
    } catch (error) {
      console.error("Erro ao buscar dados de umidade do solo:", error);
    }
  };
 
  // useEffect para buscar todos os dados quando o componente for montado
  useEffect(() => {
    fetchTemperature();
    fetchAirHumidity();
    fetchSoilMoisture();
  }, []);
 
  return (
<div style={{ display: 'flex', gap: '1.5rem', flexWrap: 'wrap', justifyContent: 'center', padding: '20px' }}>
<DataCard title="Temperatura" value={sensorData.temperature} unit="°C" icon={<FaThermometerHalf />} />
<DataCard title="Umidade do Ar" value={sensorData.airHumidity} unit="%" icon={<FaTint />} />
<DataCard title="Umidade de Solo" value={sensorData.soilMoisture} unit="%" icon={<FaWater />} />
</div>
  );
};
 
export default CardsPage;