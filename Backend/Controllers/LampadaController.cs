using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Estufa.Data;
using Estufa.Models;

namespace Estufa.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class LampadaController : ControllerBase
    {
        private readonly EstufaContext _context;

        public LampadaController(EstufaContext context)
        {
            _context = context;
        }

        // GET: api/Lampada
        [HttpGet]
        public async Task<ActionResult<IEnumerable<Lampada>>> GetLampada()
        {
            return await _context.Lampada.ToListAsync();
        }

        

        // POST: api/Lampada
        // To protect from overposting attacks, see https://go.microsoft.com/fwlink/?linkid=2123754
        [HttpPost]
        public async Task<ActionResult<Lampada>> PostLampada(Lampada lampada)
        {
            _context.Lampada.Add(lampada);
            await _context.SaveChangesAsync();

            return CreatedAtAction("GetLampada", new { id = lampada.Id }, lampada);
        }

        // DELETE: api/Lampada/5
        [HttpDelete("{id}")]
        public async Task<IActionResult> DeleteLampada(int id)
        {
            var lampada = await _context.Lampada.FindAsync(id);
            if (lampada == null)
            {
                return NotFound();
            }

            _context.Lampada.Remove(lampada);
            await _context.SaveChangesAsync();

            return NoContent();
        }

        private bool LampadaExists(int id)
        {
            return _context.Lampada.Any(e => e.Id == id);
        }
    }
}
