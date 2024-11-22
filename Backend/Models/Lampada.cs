namespace Estufa.Models
{
    public class Lampada
    {
        public int Id { get; set; }
        public required string Nome { get; set; }  // Nome da lâmpada
        public bool Status { get; set; }  // Estado atual da lâmpada (ligada/desligada)
        public DateTime UltimaAtivacao { get; set; }  // Última vez que a lâmpada foi ativada
    }
}
