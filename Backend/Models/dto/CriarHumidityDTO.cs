namespace Estufa.Models.dto
{
    public class CriarHumidityDTO
    {
        public double UmidadeAtual { get; set; }
        public double UmidadeIdeal { get; set; }

        public CriarHumidityDTO(double UmidadeAtual, double UmidadeIdeal)
        {
            this.UmidadeAtual = UmidadeAtual;
            this.UmidadeIdeal = UmidadeIdeal;
        }
    }
}
