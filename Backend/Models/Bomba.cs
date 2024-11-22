namespace Estufa.Models
{
    public class Bomba
    {
        public int Id { get; set; }
        public required string Nome { get; set; }  // Nome da bomba
        public int Quantidade { get; set; }  // Quantidade de bombas (ex: para redundância)
        public bool Status { get; set; }  // Estado atual da bomba (ligada/desligada)
        public DateTime LastActivation { get; set; }  // Última vez que a bomba foi ativada
    }
}
