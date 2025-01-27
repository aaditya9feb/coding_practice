#include <stdio.h>
#include <string.h>

typedef struct {
    char name[50];
    int runs;
    float batting_average;
    int matches_played;
} Batsman;

int main() {
    Batsman players[] = {
        {"Player A", 1200, 45.6, 30},
        {"Player B", 1500, 50.0, 35},
        {"Player C", 1100, 42.3, 25},
        {"Player D", 1300, 48.5, 28}
    };
    int num_players = sizeof(players) / sizeof(players[0]);
    Batsman best_player = players[0];

    for (int i = 1; i < num_players; i++) {
        if (players[i].batting_average > best_player.batting_average) {
            best_player = players[i];
        }
    }

    printf("Player with the best batting average:\n");
    printf("Name: %s\n", best_player.name);
    printf("Runs: %d\n", best_player.runs);
    printf("Batting Average: %.2f\n", best_player.batting_average);
    printf("Matches Played: %d\n", best_player.matches_played);

    return 0;
}
