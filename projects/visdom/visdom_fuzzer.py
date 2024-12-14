import sys
import atheris
import visdom

def fuzz_text_component(fdp):
    try:
        vis = visdom.Visdom()
        text = fdp.ConsumeUnicodeNoSurrogates(100)
        env = fdp.ConsumeUnicodeNoSurrogates(50)
        vis.text(text, env=env)
    except Exception as e:
        if "Expected error" not in str(e):
            raise

def fuzz_scatter_component(fdp):
    try:
        vis = visdom.Visdom()
        num_points = fdp.ConsumeIntInRange(1, 100)
        scatter_data = [[fdp.ConsumeFloat(), fdp.ConsumeFloat()] for _ in range(num_points)]
        vis.scatter(X=scatter_data)
    except Exception as e:
        if "Expected error" not in str(e):
            raise

def fuzz_bar_component(fdp):
    try:
        vis = visdom.Visdom()
        num_bars = fdp.ConsumeIntInRange(1, 50)
        bar_data = [fdp.ConsumeFloat() for _ in range(num_bars)]
        vis.bar(bar_data)
    except Exception as e:
        if "Expected error" not in str(e):
            raise

def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    target_function = fdp.ConsumeIntInRange(1, 3)
    if target_function == 1:
        fuzz_text_component(fdp)
    elif target_function == 2:
        fuzz_scatter_component(fdp)
    elif target_function == 3:
        fuzz_bar_component(fdp)

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
