using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Estufa.Data;
using Estufa.Models;
using Estufa.Models.dto;

namespace Estufa.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class UmidadeController : ControllerBase
    {
        private readonly EstufaContext _context;

        public UmidadeController(EstufaContext context)
        {
            _context = context;
        }

        // GET: api/Umidade
        [HttpGet]
        public async Task<ActionResult<IEnumerable<Umidade>>> GetUmidade()
        {
            return await _context.Umidade.ToListAsync();
        }

        
 // PUT: api/Umidade/5
        // To protect from overposting attacks, see https://go.microsoft.com/fwlink/?linkid=2123754
        [HttpPut("{id}")]
        public async Task<IActionResult> PutUmidade(int id, Umidade umidade)
        {
            if (id != umidade.Id)
            {
                return BadRequest();
            }
            _context.Entry(umidade).State = EntityState.Modified;
            try
            {
                await _context.SaveChangesAsync();
            }
            catch (DbUpdateConcurrencyException)
            {
                if (!UmidadeExists(id))
                {
                    return NotFound();
                }
                else
                {
                    throw;
                }
            }
            return NoContent();
        }

        // POST: api/Umidade
        // To protect from overposting attacks, see https://go.microsoft.com/fwlink/?linkid=2123754
        [HttpPost]
        public async Task<ActionResult<Umidade>> PostUmidade(CriarHumidityDTO humidityDTO)
        {
            var umidade = new Umidade
            {
                UmidadeAtual = humidityDTO.UmidadeAtual,
                UmidadeIdeal = humidityDTO.UmidadeIdeal,
                UltimaMedicao = DateTime.Now  // Definindo a data da �ltima medi��o como a data atual
            };
            _context.Umidade.Add(umidade);
            await _context.SaveChangesAsync();

            return CreatedAtAction("GetUmidade", new { id = umidade.Id }, umidade);
        }

        // DELETE: api/Umidade/5
        [HttpDelete("{id}")]
        public async Task<IActionResult> DeleteUmidade(int id)
        {
            var umidade = await _context.Umidade.FindAsync(id);
            if (umidade == null)
            {
                return NotFound();
            }

            _context.Umidade.Remove(umidade);
            await _context.SaveChangesAsync();

            return NoContent();
        }

        private bool UmidadeExists(int id)
        {
            return _context.Umidade.Any(e => e.Id == id);
        }
    }
}
