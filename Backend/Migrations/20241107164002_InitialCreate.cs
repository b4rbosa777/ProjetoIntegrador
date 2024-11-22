using System;
using Microsoft.EntityFrameworkCore.Migrations;

#nullable disable

namespace Estufa.Migrations
{
    /// <inheritdoc />
    public partial class InitialCreate : Migration
    {
        /// <inheritdoc />
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.CreateTable(
                name: "Bomba",
                columns: table => new
                {
                    Id = table.Column<int>(type: "INTEGER", nullable: false)
                        .Annotation("Sqlite:Autoincrement", true),
                    Nome = table.Column<string>(type: "TEXT", nullable: false),
                    Quantidade = table.Column<int>(type: "INTEGER", nullable: false),
                    Status = table.Column<bool>(type: "INTEGER", nullable: false),
                    LastActivation = table.Column<DateTime>(type: "TEXT", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_Bomba", x => x.Id);
                });

            migrationBuilder.CreateTable(
                name: "Lampada",
                columns: table => new
                {
                    Id = table.Column<int>(type: "INTEGER", nullable: false)
                        .Annotation("Sqlite:Autoincrement", true),
                    Nome = table.Column<string>(type: "TEXT", nullable: false),
                    Status = table.Column<bool>(type: "INTEGER", nullable: false),
                    UltimaAtivacao = table.Column<DateTime>(type: "TEXT", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_Lampada", x => x.Id);
                });

            migrationBuilder.CreateTable(
                name: "Temperatura",
                columns: table => new
                {
                    Id = table.Column<int>(type: "INTEGER", nullable: false)
                        .Annotation("Sqlite:Autoincrement", true),
                    TemperaturaAtual = table.Column<double>(type: "REAL", nullable: false),
                    TemperaturaIdeal = table.Column<double>(type: "REAL", nullable: false),
                    UltimaMedicao = table.Column<DateTime>(type: "TEXT", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_Temperatura", x => x.Id);
                });

            migrationBuilder.CreateTable(
                name: "Umidade",
                columns: table => new
                {
                    Id = table.Column<int>(type: "INTEGER", nullable: false)
                        .Annotation("Sqlite:Autoincrement", true),
                    NivelAtual = table.Column<double>(type: "REAL", nullable: false),
                    NivelIdeal = table.Column<double>(type: "REAL", nullable: false),
                    UltimaMedicao = table.Column<DateTime>(type: "TEXT", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_Umidade", x => x.Id);
                });

            migrationBuilder.CreateTable(
                name: "UmidadeTerra",
                columns: table => new
                {
                    Id = table.Column<int>(type: "INTEGER", nullable: false)
                        .Annotation("Sqlite:Autoincrement", true),
                    NivelAtual = table.Column<double>(type: "REAL", nullable: false),
                    NivelIdeal = table.Column<double>(type: "REAL", nullable: false),
                    UltimaMedicao = table.Column<DateTime>(type: "TEXT", nullable: false)
                },
                constraints: table =>
                {
                    table.PrimaryKey("PK_UmidadeTerra", x => x.Id);
                });
        }

        /// <inheritdoc />
        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropTable(
                name: "Bomba");

            migrationBuilder.DropTable(
                name: "Lampada");

            migrationBuilder.DropTable(
                name: "Temperatura");

            migrationBuilder.DropTable(
                name: "Umidade");

            migrationBuilder.DropTable(
                name: "UmidadeTerra");
        }
    }
}
