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
    public class UmidadeTerraController : ControllerBase
    {
        private readonly EstufaContext _context;

        public UmidadeTerraController(EstufaContext context)
        {
            _context = context;
        }

        // GET: api/UmidadeTerra
        [HttpGet]
        public async Task<ActionResult<IEnumerable<UmidadeTerra>>> GetUmidadeTerra()
        {
            return await _context.UmidadeTerra.ToListAsync();
        }

  
 // PUT: api/UmidadeTerra/5
        // To protect from overposting attacks, see https://go.microsoft.com/fwlink/?linkid=2123754
        [HttpPut("{id}")]
        public async Task<IActionResult> PutUmidadeTerra(int id, UmidadeTerra umidadeTerra)
        {
            if (id != umidadeTerra.Id)
            {
                return BadRequest();
            }
            _context.Entry(umidadeTerra).State = EntityState.Modified;
            try
            {
                await _context.SaveChangesAsync();
            }
            catch (DbUpdateConcurrencyException)
            {
                if (!UmidadeTerraExists(id))
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

        // POST: api/UmidadeTerra
        // To protect from overposting attacks, see https://go.microsoft.com/fwlink/?linkid=2123754
        [HttpPost]
        public async Task<ActionResult<UmidadeTerra>> PostUmidadeTerra(CriarHumidityEarthDTO humidityEarthDTO)
        {
            var umidadeTerra = new UmidadeTerra
            {
                UmidadeTerraAtual = humidityEarthDTO.UmidadeTerraAtual,
                UmidadeTerraIdeal = humidityEarthDTO.UmidadeTerraIdeal,
                UltimaMedicao = DateTime.Now  // Definindo a data da �ltima medi��o como a data atual
            };
            _context.UmidadeTerra.Add(umidadeTerra);
            await _context.SaveChangesAsync();

            return CreatedAtAction("GetUmidadeTerra", new { id = umidadeTerra.Id }, umidadeTerra);
        }

        // DELETE: api/UmidadeTerra/5
        [HttpDelete("{id}")]
        public async Task<IActionResult> DeleteUmidadeTerra(int id)
        {
            var umidadeTerra = await _context.UmidadeTerra.FindAsync(id);
            if (umidadeTerra == null)
            {
                return NotFound();
            }

            _context.UmidadeTerra.Remove(umidadeTerra);
            await _context.SaveChangesAsync();

            return NoContent();
        }

        private bool UmidadeTerraExists(int id)
        {
            return _context.UmidadeTerra.Any(e => e.Id == id);
        }
    }
}
