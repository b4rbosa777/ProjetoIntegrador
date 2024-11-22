namespace Estufa.Models.dto
{
    public class CriarHumidityEarthDTO
    {
        public double UmidadeTerraAtual { get; set; }
        public double UmidadeTerraIdeal { get; set; }

        public CriarHumidityEarthDTO(double UmidadeTerraAtual, double UmidadeTerraIdeal)
        {
            this.UmidadeTerraAtual = UmidadeTerraAtual;
            this.UmidadeTerraIdeal = UmidadeTerraIdeal;
        }
    }
}
