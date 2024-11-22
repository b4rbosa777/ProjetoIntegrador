using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace Estufa.Migrations
{
    /// <inheritdoc />
    public partial class Deploy : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.RenameColumn(
                name: "NivelIdeal",
                table: "UmidadeTerra",
                newName: "UmidadeTerraIdeal");

            migrationBuilder.RenameColumn(
                name: "NivelAtual",
                table: "UmidadeTerra",
                newName: "UmidadeTerraAtual");

            migrationBuilder.RenameColumn(
                name: "NivelIdeal",
                table: "Umidade",
                newName: "UmidadeIdeal");

            migrationBuilder.RenameColumn(
                name: "NivelAtual",
                table: "Umidade",
                newName: "UmidadeAtual");
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.RenameColumn(
                name: "UmidadeTerraIdeal",
                table: "UmidadeTerra",
                newName: "NivelIdeal");

            migrationBuilder.RenameColumn(
                name: "UmidadeTerraAtual",
                table: "UmidadeTerra",
                newName: "NivelAtual");

            migrationBuilder.RenameColumn(
                name: "UmidadeIdeal",
                table: "Umidade",
                newName: "NivelIdeal");

            migrationBuilder.RenameColumn(
                name: "UmidadeAtual",
                table: "Umidade",
                newName: "NivelAtual");
        }
    }
}
