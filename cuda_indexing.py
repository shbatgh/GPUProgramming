from manim import *

class CUDAIndexing(Scene):
    def construct(self):
        # Scene 2: Show blocks and thread indices with extra padding
        block1 = self.create_block(0, ORANGE, label_buff=0.4)
        block2 = self.create_block(1, BLUE, label_buff=0.4)
        block3 = self.create_block(2, YELLOW, label_buff=0.4)
        block4 = self.create_block(4095, RED, label_buff=0.4)

        # Create ellipsis
        ellipsis = Tex("...").scale(0.8)

        # Align the blocks horizontally, scale them down further, and adjust spacing
        blocks = VGroup(block1, block2, block3, ellipsis, block4).arrange(RIGHT, buff=0.3).scale(0.465)
        
        # Center the ellipsis both horizontally and vertically
        ellipsis_center = (block3.get_right() + block4.get_left()) / 2
        ellipsis_center += DOWN * (block3[0].get_center()[1] - block3[1].get_center()[1]) / 3
        ellipsis.move_to(ellipsis_center)

        # Add bracket from gridDim.x to blocks
        bracket = Brace(blocks, direction=UP)
        
        # Scene 1: Display gridDim.x and its value, connected to the bracket
        grid_label = Tex(r"gridDim.x = 4096").next_to(bracket, UP, buff=0.1)

        self.play(FadeIn(blocks), Create(bracket), Write(grid_label), run_time=3)
        self.wait(1)

        # Scene 3: Highlight specific thread in the last block
        highlight_thread = SurroundingRectangle(block3[1][3], color=YELLOW, buff=0.08)
        self.play(Create(highlight_thread), run_time=2)
        self.wait(1)

        # Scene 4: Show the index calculation formula with proper LaTeX formatting
        formula = Tex(r"index = blockIdx.x $\times$ blockDim.x + threadIdx.x").next_to(blocks, DOWN, buff=0.5)
        self.play(Write(formula), run_time=2)
        self.wait(1)

        # Scene 5: Substitute values and show the final index
        calculated_index = Tex(r"index = (2) $\times$ (256) + (3) = 515").next_to(formula, DOWN, buff=0.3)
        self.play(Write(calculated_index), run_time=3)
        self.wait(2)

    def create_block(self, block_idx, color, label_buff=0.4):
        """Helper function to create a block with threads, numbers, and additional padding"""
        block_label = Tex(f"blockIdx.x = {block_idx}").set_color(color)
        threads = VGroup(*[
            VGroup(
                Square().set_fill(color, opacity=0.5).scale(0.4),
                Tex(str(i) if i < 7 else '...')  # Add '...' for the second to last square
                    .scale(0.5).move_to(Square().get_center())
                if i == 5 else
                Tex('...')
                    .scale(0.5).move_to(Square().get_center())
                if i == 6 else  # Check if it's the second to last square
                Tex('255')  # Add '255' to the last square
                    .scale(0.5).move_to(Square().get_center())
                if i == 7 else
                Tex(str(i))  # For all other squares
                    .scale(0.5).move_to(Square().get_center())
            )
            for i in range(8)
        ]).arrange(RIGHT, buff=0.1)
        return VGroup(block_label, threads).arrange(DOWN, buff=label_buff)

with tempconfig({"quality": "medium_quality", "disable_caching": True}):
    scene = CUDAIndexing()
    scene.render()