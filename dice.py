# -*- coding: utf-8 -*-
"""
Professional Dice Simulator
Created on Wed Jun 11 18:54:09 2025
@author: Moreb
"""

import random
import matplotlib.pyplot as plt
import csv
from typing import Tuple, List, Dict, Optional, Any


def roll_die(sides: int = 6) -> int:
    """Simulate rolling a single die with a given number of sides.
    
    Args:
        sides: Number of sides on the die (default is 6)
        
    Returns:
        Random number between 1 and sides
    """
    if sides < 2:
        raise ValueError("Die must have at least 2 sides")
    return random.randint(1, sides)


def roll_dice(number: int = 1, sides: int = 6) -> Tuple[List[int], int]:
    """Simulate rolling multiple dice.
    
    Args:
        number: Number of dice to roll (default is 1)
        sides: Number of sides on each die (default is 6)
        
    Returns:
        tuple: (list of individual die results, total sum)
    """
    if number < 1:
        raise ValueError("Must roll at least one die")
    
    rolls = [roll_die(sides) for _ in range(number)]
    return rolls, sum(rolls)


class DiceSimulator:
    """A professional dice simulator with statistics tracking."""
    
    def __init__(self) -> None:
        self.reset_stats()
        self.rng = random.Random()  # Separate random number generator
        
    def reset_stats(self) -> None:
        """Reset all statistics."""
        self.total_rolls: int = 0
        self.roll_history: List[Tuple[int, int, List[int], int]] = []
        self.roll_counts: Dict[int, int] = {}
        
    def roll(self, number: int = 1, sides: int = 6, seed: Optional[Any] = None) -> Tuple[List[int], int]:
        """Roll dice and track statistics.
        
        Args:
            number: Number of dice to roll
            sides: Number of sides per die
            seed: Optional seed for random number generator
            
        Returns:
            tuple: (list of rolls, total sum)
        """
        if seed is not None:
            self.rng.seed(seed)
            
        rolls = [self.rng.randint(1, sides) for _ in range(number)]
        total = sum(rolls)
        
        # Update statistics
        self.total_rolls += 1
        self.roll_history.append((number, sides, rolls, total))
        
        # Track counts for each possible outcome
        for roll in rolls:
            self.roll_counts[roll] = self.roll_counts.get(roll, 0) + 1
                
        return rolls, total
    
    def get_stats(self) -> Dict[str, Any]:
        """Get current statistics.
        
        Returns:
            Dictionary containing various statistics
        """
        return {
            'total_rolls': self.total_rolls,
            'most_common': max(self.roll_counts.items(), key=lambda x: x[1]) if self.roll_counts else None,
            'roll_counts': dict(sorted(self.roll_counts.items()))
        }
    
    def probability_of(self, value: int, sides: int = 6) -> float:
        """Calculate the probability of rolling a specific value.
        
        Args:
            value: The value to calculate probability for
            sides: Number of sides on the die
            
        Returns:
            Probability between 0 and 1
        """
        if value < 1 or value > sides:
            return 0.0
        count = self.roll_counts.get(value, 0)
        return count / self.total_rolls if self.total_rolls > 0 else 0.0
    
    def plot_distribution(self, sides: Optional[int] = None) -> None:
        """Plot the distribution of dice rolls.
        
        Args:
            sides: If specified, only show distribution up to this number of sides
        """
        if not self.roll_counts:
            print("No roll data to display")
            return
            
        # Prepare data
        max_side = sides or max(self.roll_counts.keys())
        x = range(1, max_side + 1)
        y = [self.roll_counts.get(i, 0) for i in x]
        
        # Create plot
        plt.figure(figsize=(10, 6))
        plt.bar(x, y)
        plt.title(f"Dice Roll Distribution (Total Rolls: {self.total_rolls})")
        plt.xlabel("Dice Value")
        plt.ylabel("Frequency")
        plt.xticks(x)
        plt.grid(axis='y', alpha=0.75)
        plt.show()
    
    def export_history(self, filename: str) -> None:
        """Export roll history to a CSV file.
        
        Args:
            filename: Path to the output file
        """
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Roll #', 'Number of Dice', 'Sides', 'Rolls', 'Total'])
            for i, (num, sides, rolls, total) in enumerate(self.roll_history, 1):
                writer.writerow([i, num, sides, ' '.join(map(str, rolls)), total])


if __name__ == "__main__":
    # Create simulator instance
    simulator = DiceSimulator()
    
    # Roll some dice
    for _ in range(1000):
        simulator.roll(number=2, sides=6)  # Roll 2d6
        
    # Get statistics
    stats = simulator.get_stats()
    print(f"Total rolls: {stats['total_rolls']}")
    print(f"Most common roll: {stats['most_common']}")
    
    # View probability of rolling a 7 (with 2d6)
    print(f"Probability of 7: {simulator.probability_of(7):.2%}")
    
    # Visualize the distribution
    simulator.plot_distribution()
    
    # Export history to file
    simulator.export_history("dice_roll_history.csv")