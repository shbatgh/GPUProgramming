from manim import *

class CPUvsGPU(Scene):
    def construct(self):
        cpu_rects = []
        cpu_texts = []

        def create_alu():
            alu = Rectangle(width=1, height=1, color=BLUE, fill_opacity=0.5)
            sw = 0.04
            cpu_rects.append(alu)
            alu_text = Text("Core", font_size=14).move_to(alu.get_center())
            cpu_texts.append(alu_text)

            cache = Rectangle(width=1, height=0.25, fill_opacity=0.5, color=RED).next_to(alu, DOWN, aligned_edge=LEFT, buff=sw)
            cpu_rects.append(cache)
            cache_text = Text("L1 Cache", font_size=14).move_to(cache.get_center())
            cpu_texts.append(cache_text)

            control = Rectangle(width=0.5, height=1.25+sw, color=PURPLE, fill_opacity=0.5).next_to(alu, RIGHT, aligned_edge=UP, buff=sw)
            cpu_rects.append(control)
            control_text1 = Text("Con", font_size=14)
            control_text2 = Text("trol", font_size=14)
            ct = VGroup(control_text1, control_text2).arrange(DOWN, buff=0.05).move_to(control)
            cpu_texts.append(control_text1)
            cpu_texts.append(control_text2)
            return VGroup(alu, alu_text, cache, cache_text, control, ct)

        alu1 = create_alu().shift(4*LEFT+UP)
        alu2 = create_alu().next_to(alu1, RIGHT, buff=0.1)
        alu3 = create_alu().next_to(alu1, DOWN, aligned_edge=LEFT, buff=0.1)
        alu4 = create_alu().next_to(alu3, RIGHT, buff=0.1)

        cache1 = Rectangle(width=alu1.width, height=0.4, color=RED, fill_opacity=0.5).next_to(alu3, DOWN, aligned_edge=LEFT, buff=0.1)
        cache2 = Rectangle(width=alu1.width, height=0.4, color=RED, fill_opacity=0.5).next_to(alu4, DOWN, aligned_edge=LEFT, buff=0.1)
        cpu_rects.append(cache1)
        cpu_rects.append(cache2)
        cpu_texts.append(Text("L2 Cache", font_size=14).move_to(cache1))
        cpu_texts.append(Text("L2 Cache", font_size=14).move_to(cache2))

        cache3 = Rectangle(width=cache1.width*2 + 0.1, height=0.5, color=RED, fill_opacity=0.5).next_to(cache1, DOWN, aligned_edge=LEFT, buff=0.1)
        cpu_rects.append(cache3)
        cpu_texts.append(Text("L3 Cache", font_size=14).move_to(cache3))

        dram_cpu = Rectangle(width=cache3.width, height=0.7, color=GREEN, fill_opacity=0.5).next_to(cache3, DOWN, buff=0.1).align_to(alu3, LEFT)
        dram_cpu_text = Text("DRAM", font_size=24).move_to(dram_cpu.get_center())
        cpu_rects.append(dram_cpu)
        cpu_texts.append(dram_cpu_text)

        gpu_rects = []
        gpu_texts = []
        gpu_alu_list = []
        for _ in range(5):
            cc = VGroup(
                Rectangle(width=0.5, height=0.2, color=PURPLE, fill_opacity=0.5),
                Rectangle(width=0.5, height=0.2, color=RED, fill_opacity=0.5)
            ).arrange(DOWN, buff=0.1)
            gpu_rects.append(cc[0])
            gpu_rects.append(cc[1])
            alus = [Rectangle(width=0.5, height=0.5, color=BLUE, fill_opacity=0.5) for _ in range(8)]
            gpu_rects.extend(alus)
            gpu_alu_list.append(VGroup(cc, *alus).arrange(RIGHT, buff=0.1))
        gpu_alus = VGroup(*gpu_alu_list).scale(0.8).arrange(DOWN, buff=0.16)

        l2 = Rectangle(width=4.25, height=0.4, color=RED, fill_opacity=0.5).match_width(gpu_alus).next_to(gpu_alus, DOWN, buff=0.1)
        gpu_rects.append(l2)
        l2_text = Text("L2 Cache", font_size=14).move_to(l2)
        gpu_texts.append(l2_text)

        dram_gpu = Rectangle(width=4.25, height=0.5, color=GREEN, fill_opacity=0.5).match_width(gpu_alus).next_to(l2, DOWN, buff=0.1)
        gpu_rects.append(dram_gpu)
        dram_gpu_text = Text("DRAM", font_size=14).move_to(dram_gpu.get_center())
        gpu_texts.append(dram_gpu_text)

        cpu = VGroup(*cpu_rects, *cpu_texts, dram_cpu, dram_cpu_text)
        gpu = VGroup(gpu_alus, l2, l2_text, dram_gpu, dram_gpu_text).match_height(cpu)

        cpu_title = Text("CPU").scale(0.8).next_to(cpu, UP)
        gpu_title = Text("GPU").scale(0.8).next_to(gpu, UP)

        # Create groups with titles
        cpu_group = VGroup(cpu_title, cpu)
        gpu_group = VGroup(gpu_title, gpu)

        # Arrange CPU and GPU groups side by side
        full_diagram = VGroup(cpu_group, gpu_group).arrange(RIGHT, buff=1)

        # Center the entire diagram vertically
        full_diagram.center()

        # Add objects to the scene
        self.play(*[Create(x) for x in cpu_rects])
        self.play(*[Write(x) for x in cpu_texts])
        self.play(Write(cpu_title))
        self.wait(1)

        self.play(*[Create(x) for x in gpu_rects])
        self.play(*[Write(x) for x in gpu_texts])
        self.play(Write(gpu_title))
        self.wait(2)

        # Optional: You can save the scene as a PNG if you want
        # self.camera.frame.save_state()
        # self.camera.frame.move_to(full_diagram.get_center())
        # self.add(full_diagram)
        # self.wait(1)
        # self.get_frame().save_image("cpu_vs_gpu.png")