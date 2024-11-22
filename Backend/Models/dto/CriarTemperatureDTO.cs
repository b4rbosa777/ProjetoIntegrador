namespace Estufa.Models.dto
{
    public class CriarTemperatureDTO
    {
        public double TemperaturaAtual { get; set; }
        public double TemperaturaIdeal { get; set; }

        public CriarTemperatureDTO( double TemperaturaAtual, double TemperaturaIdeal) { 
            this.TemperaturaAtual = TemperaturaAtual;
            this.TemperaturaIdeal = TemperaturaIdeal;
        }
    }
}
