import CodeBlock from "@/app/components/codeblock";

export default function Page() {
  return (
    <div className="blog-content">
      <h2 className="mb-2 text-xl font-semibold">
        Improving Diarization with LLMs: A Journey through nbdev and Claude
      </h2>
      <div className="indent-4 opacity-60">July 6, 2024</div>
      <p>
        If you enjoy programming Python in notebooks (which I do, despite the
        potential complexities when creating artifacts) and appreciate good,
        &ldquo;automatically&rdquo; generated documentation hosted on a website,
        you might find nbdev intriguing.
      </p>
      <p>
        For more information, visit:{" "}
        <a href="https://nbdev.fast.ai/">nbdev.fast.ai</a>
      </p>
      <p>
        For the small price of adding various annotations to your notebook to
        export only the proper module while simultaneously generating
        documentation, you gain commands that will publish the exported module
        to PyPI and Conda, along with a GitHub Pages site hosting your
        documentation in a pleasant format. There&apos;s much more to explore in
        their documentation:
      </p>
      <p>
        <a href="https://nbdev.fast.ai/getting_started.html">
          nbdev.fast.ai/getting_started.html
        </a>
      </p>
      <p>
        I mention this because I recently had the opportunity to try improving
        diarization with LLMs (credit to{" "}
        <a href="https://arxiv.org/html/2401.03506v4">this paper</a> for the
        idea) while also satisfying my curiosity about nbdev. This project
        aligned nicely with my recent enjoyment of{" "}
        <a href="https://claudette.answer.ai/">Claudette</a>, which works great
        in a notebook and serves as an excellent replacement for Claude&apos;s
        website UI when I encounter throttling issues.
      </p>
      <h3 className="mb-2 mt-4 text-lg font-semibold">
        Improving Diarization with LLMs
      </h3>
      <p>
        I started working with Claude Sonnet 3.5, primarily because it&apos;s
        the latest model and Claudette makes it simple to use. The main
        mechanism, well-explained in the paper I mentioned earlier, involves
        prompting the model with a transcript containing speech attribution and
        asking it to identify and fix diarization mistakes.
      </p>
      <p>
        I found that providing examples of common error types improved results.
        Here are some examples:
      </p>
      <h4 className="text-md mb-1 mt-3 font-semibold">Bleeding:</h4>
      <CodeBlock
        code={`
Speaker1: Hi my name is David. Hi my
Speaker2: name is David also
        `}
      />
      <h4 className="text-md mb-1 mt-3 font-semibold">Burying:</h4>
      <CodeBlock
        code={`
Speaker1: Hi how are you? I'm fine, thanks! How are you? I'm doing well.
Speaker2: How's the weather over there?...
        `}
      />
      <p>
        However, as with many LLM applications, context is crucial. Since
        we&apos;re primarily interested in diarizing long conversational content
        (10+ hours), we need to develop a strategy that acknowledges the
        limitations of the models we&apos;re using and finds ways to accommodate
        those limitations.
      </p>
      <p>
        Firstly, it&apos;s cost-prohibitive to maximize the context for every
        interaction with the model. If your conversation has 1 million tokens
        and the model has a 200k context window, by the time your back-and-forth
        reaches that window, the model&apos;s inference from that full context
        becomes much more expensive. Depending on your chosen chunk size, this
        could happen for another 40 interactions.
      </p>
      <p>
        One solution is to reset the context occasionally while modifying the
        prompt to inform the model that it&apos;s processing mid-conversation
        data. That&apos;s the approach I took.
      </p>
      <p>You can explore my diarization with LLM package here:</p>
      <p>
        <a href="https://github.com/russedavid/improve-diarization-with-llm">
          github.com/russedavid/improve-diarization-with-llm
        </a>
      </p>
      <p>And find the documentation here:</p>
      <p>
        <a href="https://russedavid.github.io/improve-diarization-with-llm/">
          russedavid.github.io/improve-diarization-with-llm/
        </a>
      </p>
    </div>
  );
}
