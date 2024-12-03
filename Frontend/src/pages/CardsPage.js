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

  // Função para buscar todos os dados (temperatura, umidade do ar, umidade do solo)
  const fetchAllData = async () => {
    try {
      // Buscar temperatura
      const temperatureResponse = await axios.get('http://localhost:5271/api/Temperatura');
      const lastTemperature = temperatureResponse.data && temperatureResponse.data.length > 0 
        ? temperatureResponse.data[temperatureResponse.data.length - 1] 
        : null;

      // Buscar umidade do ar
      const airHumidityResponse = await axios.get('http://localhost:5271/api/Umidade');
      const lastAirHumidity = airHumidityResponse.data && airHumidityResponse.data.length > 0 
        ? airHumidityResponse.data[airHumidityResponse.data.length - 1] 
        : null;

      // Buscar umidade do solo
      const soilMoistureResponse = await axios.get('http://localhost:5271/api/UmidadeTerra');
      const lastSoilMoisture = soilMoistureResponse.data && soilMoistureResponse.data.length > 0 
        ? soilMoistureResponse.data[soilMoistureResponse.data.length - 1] 
        : null;

      // Atualizar o estado com os dados mais recentes
      setSensorData({
        temperature: lastTemperature?.temperaturaAtual || 0,
        airHumidity: lastAirHumidity?.umidadeAtual || 0,
        soilMoisture: lastSoilMoisture?.umidadeTerraAtual || 0,
      });
    } catch (error) {
      console.error('Erro ao buscar dados da API:', error);
    }
  };

  // useEffect para iniciar a atualização automática
  useEffect(() => {
    // Buscar os dados imediatamente ao montar o componente
    fetchAllData();

    // Configurar o intervalo para atualizar os dados a cada 1 segundo
    const intervalId = setInterval(() => {
      fetchAllData();
    }, 1000); // 1 segundo

    // Limpar o intervalo ao desmontar o componente
    return () => clearInterval(intervalId);
  }, []);

  return (
    <div
      style={{
        display: 'flex',
        gap: '1.5rem',
        flexWrap: 'wrap',
        justifyContent: 'center',
        padding: '20px',
      }}
    >
      <DataCard title="Temperatura" value={sensorData.temperature} unit="°C" icon={<FaThermometerHalf />} />
      <DataCard title="Umidade do Ar" value={sensorData.airHumidity} unit="%" icon={<FaTint />} />
      <DataCard title="Umidade do Solo" value={sensorData.soilMoisture} unit="%" icon={<FaWater />} />
    </div>
  );
};

export default CardsPage;