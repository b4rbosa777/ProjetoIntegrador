using Estufa.Models.dto;

namespace Estufa.Models
{
    public class UmidadeTerra
    {
        public int Id { get; set; }
        public double UmidadeTerraAtual { get; set; }  // Nível de umidade do solo atual
        public double UmidadeTerraIdeal { get; set; }  // Nível ideal de umidade do solo
        public DateTime UltimaMedicao { get; set; }  // Data e hora da última medição

        public CriarHumidityEarthDTO mapToDto()
        {
            return new CriarHumidityEarthDTO(this.UmidadeTerraAtual, this.UmidadeTerraIdeal);
        }
    }
}
