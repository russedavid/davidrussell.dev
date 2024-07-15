import CodeBlock from "@/app/components/codeblock";

export default function Page() {
  return (
    <div className="blog-content">
      <h2 className="mb-2 text-xl font-semibold">
        Formatting Conversation Dataset for Fine-tuning: A Tool for Preparing Your Data
      </h2>
      <div className="indent-4 opacity-60">July 14, 2024</div>
      <p>
        You&apos;ve transcribed, diarized, and maybe even gone to some lengths to improve the quality of the diarization further with an LLM. So now you&apos;re ready to finetune a model with your data, right? Not quite.
      </p>
      <p>
        You still need to put the information in a format suited to fine-tuning your model. <a href="https://platform.openai.com/docs/guides/fine-tuning/preparing-your-dataset">OpenAI has a guide to this</a>, but in short, you need to turn your conversational data into something that looks like this:
      </p>
      <CodeBlock
        code={`
{"messages": [{"role": "system", "content": "Marv is a factual chatbot that is also sarcastic."}, {"role": "user", "content": "What's the capital of France?"}, {"role": "assistant", "content": "Paris, as if everyone doesn't know that already."}]}
{"messages": [{"role": "system", "content": "Marv is a factual chatbot that is also sarcastic."}, {"role": "user", "content": "Who wrote 'Romeo and Juliet'?"}, {"role": "assistant", "content": "Oh, just some guy named William Shakespeare. Ever heard of him?"}]}
{"messages": [{"role": "system", "content": "Marv is a factual chatbot that is also sarcastic."}, {"role": "user", "content": "How far is the Moon from Earth?"}, {"role": "assistant", "content": "Around 384,400 kilometers. Give or take a few, like that really matters."}]}
        `}
      />
      <p>
        Obviously, I need to do this too! So I made a tool that works nicely for my usecase.
      </p>
      <p>
        Here are the docs:{" "}
        <br/>
        <a href="https://russedavid.github.io/format_conversation_dataset/">
          russedavid.github.io/format_conversation_dataset/
        </a>
      </p>
      <p>
        and here&apos;s the github repo:{" "}
        <br/>
        <a href="https://github.com/russedavid/format_conversation_dataset">
          github.com/russedavid/format_conversation_dataset
        </a>
      </p>
      <p>
        The way my diarized transcription is outputted, I have a speaker on each line. Since I&apos;m trying to get the model to emulate one of the speakers only, my formatter will take as an input a 2 digit string representation of the speaker &ldquo;number&rdquo;, like &ldquo;02&rdquo; and use that to designate that speaker as the &lsquo;assistant&rsquo; for formatting purposes. Then, all of the other speakers, their label and their content will be concat&apos;ed together till the next assistant line.
      </p>
      <p>
        There&apos;s an optional context parameter as well if you want to provide a system input at the beginning helping to explain the assistant&apos;s role in the conversation.
      </p>
    </div>
  );
}
