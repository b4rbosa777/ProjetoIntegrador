using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;
using Estufa.Models;

namespace Estufa.Data
{
    public class EstufaContext : DbContext
    {
        public EstufaContext (DbContextOptions<EstufaContext> options)
            : base(options)
        {
        }

        public DbSet<Estufa.Models.Bomba> Bomba { get; set; } = default!;
        public DbSet<Estufa.Models.Umidade> Umidade { get; set; } = default!;
        public DbSet<Estufa.Models.UmidadeTerra> UmidadeTerra { get; set; } = default!;
        public DbSet<Estufa.Models.Lampada> Lampada { get; set; } = default!;
        public DbSet<Estufa.Models.Temperatura> Temperatura { get; set; } = default!;
        public DbSet<Estufa.Models.Login> Login { get; set; } = default!;
    }
}
