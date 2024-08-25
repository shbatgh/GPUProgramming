from manim import *

class ParallelThreads(Scene):
    def construct(self):
        # Scene 1: Single thread
        single_thread = Square().set_fill(RED, opacity=0.5).scale(0.5)
        thread_label = Text("Thread").next_to(single_thread, UP)
        self.play(FadeIn(single_thread), Write(thread_label))
        self.wait(1)

        # Scene 2: Replace the old text with "Block"
        block_group = VGroup(single_thread, thread_label)
        block_threads = VGroup(*[Square().set_fill(RED, opacity=0.5).scale(0.5) for _ in range(4)]).arrange(RIGHT)
        block_label = Text("Block").next_to(block_threads, UP)
        
        self.play(Transform(block_group, VGroup(block_threads, block_label)))
        self.wait(1)

        # Scene 3: Replace with "Grid"
        grid_blocks = VGroup(*[VGroup(*[Square().set_fill(RED, opacity=0.5).scale(0.5) for _ in range(4)]).arrange(RIGHT) for _ in range(4)]).arrange(DOWN)
        grid_label = Text("Grid").next_to(grid_blocks, UP)
        
        self.play(Transform(block_group, VGroup(grid_blocks, grid_label)))
        self.wait(2)
